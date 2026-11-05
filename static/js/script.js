/**
 * Smart Review Analyzer - JavaScript
 * Handles client-side interactions and form submissions
 */

// Global configuration
const CONFIG = {
    API_ENDPOINT: '/analyze',
    MAX_FILE_SIZE: 16 * 1024 * 1024, // 16MB
    CHUNK_SIZE: 1000, // Process reviews in chunks
};

// ============================================
// Form Validation
// ============================================

/**
 * Validate CSV file
 */
function validateCsvFile(file) {
    if (!file) {
        return { valid: false, message: 'No file selected' };
    }

    if (!file.name.toLowerCase().endsWith('.csv')) {
        return { valid: false, message: 'Please select a CSV file' };
    }

    if (file.size > CONFIG.MAX_FILE_SIZE) {
        return { valid: false, message: `File size exceeds ${CONFIG.MAX_FILE_SIZE / 1024 / 1024}MB limit` };
    }

    return { valid: true };
}

/**
 * Validate manual text input
 */
function validateManualText(text) {
    if (!text || text.trim().length === 0) {
        return { valid: false, message: 'Please enter at least one review' };
    }

    const reviews = text.split('\n').filter(r => r.trim().length > 0);
    if (reviews.length === 0) {
        return { valid: false, message: 'Please enter at least one review' };
    }

    return { valid: true, reviews: reviews.length };
}

// ============================================
// File Handling
// ============================================

/**
 * Handle file selection
 */
document.addEventListener('DOMContentLoaded', function() {
    const csvFileInput = document.getElementById('csvFile');
    if (csvFileInput) {
        csvFileInput.addEventListener('change', function(e) {
            const validation = validateCsvFile(this.files[0]);
            if (!validation.valid) {
                console.warn(validation.message);
            }
        });
    }
});

/**
 * Download sample CSV file
 */
function downloadSample() {
    fetch('/api/sample-data')
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'sample_reviews.csv');
            document.body.appendChild(link);
            link.click();
            link.parentNode.removeChild(link);
            window.URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error('Error downloading sample:', error);
            showAlert('Error downloading sample file: ' + error.message, 'danger');
        });
}

// ============================================
// Form Submission
// ============================================

/**
 * Handle CSV form submission
 */
const csvForm = document.getElementById('csvForm');
if (csvForm) {
    csvForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const fileInput = document.getElementById('csvFile');
        const validation = validateCsvFile(fileInput.files[0]);

        if (!validation.valid) {
            showAlert(validation.message, 'danger');
            return;
        }

        submitAnalysis(this);
    });
}

/**
 * Handle manual form submission
 */
const manualForm = document.getElementById('manualForm');
if (manualForm) {
    manualForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const textInput = document.getElementById('manualText').value;
        const validation = validateManualText(textInput);

        if (!validation.valid) {
            showAlert(validation.message, 'danger');
            return;
        }

        showAlert(`Preparing to analyze ${validation.reviews} review(s)...`, 'info');
        submitAnalysis(this);
    });
}

/**
 * Submit analysis request
 */
function submitAnalysis(form) {
    const formData = new FormData(form);

    // Show loading modal
    const loadingModal = document.getElementById('loadingModal');
    if (loadingModal) {
        const modal = new bootstrap.Modal(loadingModal);
        modal.show();
    }

    fetch(CONFIG.API_ENDPOINT, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || 'Analysis failed');
                });
            }
            return response.json();
        })
        .then(data => {
            console.log('Analysis successful:', data);

            // Hide loading modal
            if (loadingModal) {
                const modal = bootstrap.Modal.getInstance(loadingModal);
                if (modal) modal.hide();
            }

            // Store results
            localStorage.setItem('analysisResults', JSON.stringify(data));

            // Show success alert
            showAlert(`Analysis complete! Processed ${data.total_reviews} reviews.`, 'success');

            // Scroll to results or redirect
            setTimeout(() => {
                window.location.href = '/results';
            }, 1500);
        })
        .catch(error => {
            console.error('Error:', error);

            // Hide loading modal
            if (loadingModal) {
                const modal = bootstrap.Modal.getInstance(loadingModal);
                if (modal) modal.hide();
            }

            showAlert('Error: ' + error.message, 'danger');
        });
}

// ============================================
// Utilities
// ============================================

/**
 * Show alert message
 */
function showAlert(message, type = 'info') {
    // Create alert element if not exists
    let alertContainer = document.getElementById('alertContainer');
    if (!alertContainer) {
        alertContainer = document.createElement('div');
        alertContainer.id = 'alertContainer';
        alertContainer.style.position = 'fixed';
        alertContainer.style.top = '100px';
        alertContainer.style.right = '20px';
        alertContainer.style.zIndex = '9999';
        alertContainer.style.maxWidth = '400px';
        document.body.appendChild(alertContainer);
    }

    // Create alert
    const alertId = 'alert-' + Date.now();
    const alertHTML = `
        <div id="${alertId}" class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    alertContainer.innerHTML += alertHTML;

    // Auto-remove after 5 seconds
    setTimeout(() => {
        const alert = document.getElementById(alertId);
        if (alert) {
            alert.remove();
        }
    }, 5000);
}

/**
 * Format percentage
 */
function formatPercent(value) {
    return parseFloat(value).toFixed(2) + '%';
}

/**
 * Format number
 */
function formatNumber(num) {
    return new Intl.NumberFormat('en-US').format(num);
}

/**
 * Format date
 */
function formatDate(date) {
    return new Date(date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

/**
 * Debounce function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Throttle function
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// ============================================
// LocalStorage Management
// ============================================

/**
 * Save data to localStorage
 */
function saveToStorage(key, data) {
    try {
        localStorage.setItem(key, JSON.stringify(data));
        return true;
    } catch (error) {
        console.error('Error saving to storage:', error);
        return false;
    }
}

/**
 * Get data from localStorage
 */
function getFromStorage(key) {
    try {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : null;
    } catch (error) {
        console.error('Error reading from storage:', error);
        return null;
    }
}

/**
 * Clear localStorage
 */
function clearStorage() {
    try {
        localStorage.clear();
        return true;
    } catch (error) {
        console.error('Error clearing storage:', error);
        return false;
    }
}

// ============================================
// Event Listeners
// ============================================

// Log page visibility changes
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        console.log('Page hidden');
    } else {
        console.log('Page visible');
    }
});

// Log unload
window.addEventListener('beforeunload', function() {
    // Save any unsaved data
    console.log('Page unloading');
});

// ============================================
// Initialization
// ============================================

console.log('Smart Review Analyzer loaded successfully');
