"""
Product Recommendation Engine
Recommends products based on sentiment analysis
"""


class RecommendationEngine:
    """
    Recommends products based on sentiment scores
    """
    
    def __init__(self, threshold_positive=0.05):
        """
        Initialize recommendation engine
        
        Args:
            threshold_positive (float): Compound score threshold for positive sentiment
        """
        self.threshold_positive = threshold_positive
    
    def calculate_product_scores(self, reviews_data):
        """
        Calculate aggregated sentiment scores for each product
        
        Args:
            reviews_data (list): List of dicts with 'product', 'review', 'sentiment'
            
        Returns:
            dict: Product names mapped to sentiment statistics
        """
        products = {}
        
        for item in reviews_data:
            product = item.get('product', 'Unknown Product')
            sentiment = item.get('sentiment', {})
            compound = sentiment.get('compound', 0)
            label = sentiment.get('label', 'neutral')
            
            if product not in products:
                products[product] = {
                    'reviews': [],
                    'positive_count': 0,
                    'negative_count': 0,
                    'neutral_count': 0,
                    'total_reviews': 0,
                    'average_score': 0
                }
            
            products[product]['reviews'].append(compound)
            products[product]['total_reviews'] += 1
            
            if label == 'positive':
                products[product]['positive_count'] += 1
            elif label == 'negative':
                products[product]['negative_count'] += 1
            else:
                products[product]['neutral_count'] += 1
        
        # Calculate averages and percentages
        for product in products:
            scores = products[product]['reviews']
            total = products[product]['total_reviews']
            
            products[product]['average_score'] = round(sum(scores) / total, 3) if total > 0 else 0
            products[product]['positive_percentage'] = round(
                (products[product]['positive_count'] / total) * 100, 2
            ) if total > 0 else 0
            products[product]['negative_percentage'] = round(
                (products[product]['negative_count'] / total) * 100, 2
            ) if total > 0 else 0
            
            # Remove reviews list to reduce data size
            del products[product]['reviews']
        
        return products
    
    def get_top_recommendations(self, products_data, top_n=5):
        """
        Get top recommended products based on sentiment
        
        Args:
            products_data (dict): Product sentiment statistics
            top_n (int): Number of top products to return
            
        Returns:
            list: Top recommended products
        """
        # Sort products by average score (descending)
        sorted_products = sorted(
            products_data.items(),
            key=lambda x: x[1]['average_score'],
            reverse=True
        )
        
        # Filter positive products and get top N
        top_products = []
        for product, stats in sorted_products[:top_n]:
            if stats['average_score'] >= self.threshold_positive:
                top_products.append({
                    'product': product,
                    'average_score': stats['average_score'],
                    'positive_percentage': stats['positive_percentage'],
                    'total_reviews': stats['total_reviews'],
                    'positive_count': stats['positive_count']
                })
        
        return top_products
    
    def get_recommendations(self, reviews_data, top_n=5):
        """
        Generate product recommendations from reviews
        
        Args:
            reviews_data (list): Raw review data with sentiment
            top_n (int): Number of recommendations
            
        Returns:
            dict: Recommendations and product scores
        """
        # Calculate product scores
        products = self.calculate_product_scores(reviews_data)
        
        # Get top recommendations
        recommendations = self.get_top_recommendations(products, top_n)
        
        return {
            'recommendations': recommendations,
            'product_scores': products,
            'total_products': len(products)
        }
    
    def get_worst_products(self, products_data, top_n=5):
        """
        Get products with worst sentiment (for warnings)
        
        Args:
            products_data (dict): Product sentiment statistics
            top_n (int): Number of products to return
            
        Returns:
            list: Worst rated products
        """
        # Sort by average score (ascending)
        sorted_products = sorted(
            products_data.items(),
            key=lambda x: x[1]['average_score']
        )
        
        worst_products = []
        for product, stats in sorted_products[:top_n]:
            if stats['average_score'] < 0:  # Only include negative products
                worst_products.append({
                    'product': product,
                    'average_score': stats['average_score'],
                    'negative_percentage': stats['negative_percentage'],
                    'total_reviews': stats['total_reviews']
                })
        
        return worst_products
