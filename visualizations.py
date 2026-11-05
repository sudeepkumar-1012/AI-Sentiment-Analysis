"""
Visualization Module
Creates charts and graphs for sentiment analysis results
"""

import matplotlib.pyplot as plt
import io
import base64
from collections import defaultdict


def create_sentiment_chart(sentiment_summary):
    """
    Create a pie chart for sentiment distribution
    
    Args:
        sentiment_summary (dict): Summary of sentiment analysis
        
    Returns:
        str: Base64 encoded image
    """
    try:
        # Prepare data
        labels = ['Positive', 'Negative', 'Neutral']
        sizes = [
            sentiment_summary['positive_count'],
            sentiment_summary['negative_count'],
            sentiment_summary['neutral_count']
        ]
        colors = ['#2ecc71', '#e74c3c', '#95a5a6']
        explode = (0.05, 0.05, 0)
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Create pie chart
        wedges, texts, autotexts = ax.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            shadow=True,
            startangle=90,
            textprops={'fontsize': 12, 'weight': 'bold'}
        )
        
        # Add title
        ax.set_title('Sentiment Distribution', fontsize=14, weight='bold', pad=20)
        
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')
        
        # Save to bytes
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
        img_buffer.seek(0)
        
        # Convert to base64
        img_str = base64.b64encode(img_buffer.getvalue()).decode()
        plt.close()
        
        return f"data:image/png;base64,{img_str}"
    
    except Exception as e:
        print(f"Error creating sentiment chart: {e}")
        return None


def create_bar_chart(data, title, xlabel, ylabel):
    """
    Create a horizontal bar chart
    
    Args:
        data (dict): Dictionary with labels and values
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        
    Returns:
        str: Base64 encoded image
    """
    try:
        # Prepare data
        labels = list(data.keys())
        values = list(data.values())
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create bar chart
        colors = ['#3498db' if v >= 0 else '#e74c3c' for v in values]
        ax.barh(labels, values, color=colors)
        
        # Add labels and title
        ax.set_xlabel(xlabel, fontsize=12, weight='bold')
        ax.set_ylabel(ylabel, fontsize=12, weight='bold')
        ax.set_title(title, fontsize=14, weight='bold', pad=20)
        
        # Add value labels on bars
        for i, v in enumerate(values):
            ax.text(v + 0.02, i, f'{v:.2f}', va='center', fontsize=10, weight='bold')
        
        plt.tight_layout()
        
        # Save to bytes
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
        img_buffer.seek(0)
        
        # Convert to base64
        img_str = base64.b64encode(img_buffer.getvalue()).decode()
        plt.close()
        
        return f"data:image/png;base64,{img_str}"
    
    except Exception as e:
        print(f"Error creating bar chart: {e}")
        return None


def create_product_chart(reviews_data):
    """
    Create a chart showing sentiment by product
    
    Args:
        reviews_data (list): List of review dictionaries with product and sentiment
        
    Returns:
        str: Base64 encoded image
    """
    try:
        # Aggregate sentiment by product
        product_scores = defaultdict(list)
        product_sentiments = defaultdict(lambda: {'positive': 0, 'negative': 0, 'neutral': 0})
        
        for review in reviews_data:
            if 'product' in review:
                product = review['product']
                sentiment_label = review['label']
                compound = review['sentiment']['compound']
                
                product_scores[product].append(compound)
                product_sentiments[product][sentiment_label] += 1
        
        # Calculate average scores
        avg_scores = {}
        for product, scores in product_scores.items():
            avg_scores[product] = sum(scores) / len(scores)
        
        # Create bar chart with average scores
        return create_bar_chart(
            avg_scores,
            'Average Sentiment Score by Product',
            'Average Compound Score',
            'Product'
        )
    
    except Exception as e:
        print(f"Error creating product chart: {e}")
        return None


def create_stacked_bar_chart(reviews_data):
    """
    Create a stacked bar chart showing sentiment distribution by product
    
    Args:
        reviews_data (list): List of review dictionaries
        
    Returns:
        str: Base64 encoded image
    """
    try:
        # Aggregate sentiment counts by product
        product_sentiments = defaultdict(lambda: {'positive': 0, 'negative': 0, 'neutral': 0})
        
        for review in reviews_data:
            if 'product' in review:
                product = review['product']
                sentiment_label = review['label']
                product_sentiments[product][sentiment_label] += 1
        
        # Prepare data for stacked bar chart
        products = list(product_sentiments.keys())
        positive_counts = [product_sentiments[p]['positive'] for p in products]
        negative_counts = [product_sentiments[p]['negative'] for p in products]
        neutral_counts = [product_sentiments[p]['neutral'] for p in products]
        
        # Create stacked bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        
        x_pos = range(len(products))
        width = 0.6
        
        ax.bar(x_pos, positive_counts, width, label='Positive', color='#2ecc71')
        ax.bar(x_pos, negative_counts, width, bottom=positive_counts, label='Negative', color='#e74c3c')
        
        bottom_vals = [p + n for p, n in zip(positive_counts, negative_counts)]
        ax.bar(x_pos, neutral_counts, width, bottom=bottom_vals, label='Neutral', color='#95a5a6')
        
        # Add labels and title
        ax.set_ylabel('Number of Reviews', fontsize=12, weight='bold')
        ax.set_xlabel('Product', fontsize=12, weight='bold')
        ax.set_title('Sentiment Distribution by Product', fontsize=14, weight='bold', pad=20)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(products, rotation=45, ha='right')
        ax.legend()
        
        plt.tight_layout()
        
        # Save to bytes
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
        img_buffer.seek(0)
        
        # Convert to base64
        img_str = base64.b64encode(img_buffer.getvalue()).decode()
        plt.close()
        
        return f"data:image/png;base64,{img_str}"
    
    except Exception as e:
        print(f"Error creating stacked bar chart: {e}")
        return None
