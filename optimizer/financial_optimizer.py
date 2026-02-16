from typing import List, Dict
import logging
from .data_fetcher import MarketDataFetcher
from .strategy_generator import StrategyGenerator

class FinancialStrategyOptimizer:
    def __init__(self):
        self.data_fetcher = MarketDataFetcher()
        self.strategy_generator = StrategyGenerator()
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def optimize_strategies(self) -> List[Dict]:
        """
        Fetches market data, generates strategies, evaluates them, and returns the optimal ones.
        """
        try:
            # Step 1: Fetch Market Data
            data = self.data_fetcher.fetch_data()
            if not data:
                raise ValueError("No market data fetched.")
                
            # Step 2: Generate Strategies
            strategies = self.strategy_generator.generate(strategies_data=data)
            
            # Step 3: Evaluate Strategies
            evaluated_strategies = []
            for strategy in strategies:
                evaluation = self._evaluate_strategy(strategy)
                if evaluation.get('score', 0) > 50:  # Arbitrary threshold
                    evaluated_strategies.append({
                        'strategy_id': strategy['id'],
                        'evaluation_score': evaluation['score']
                    })
                    
            return evaluated_strategies
            
        except Exception as e:
            self.logger.error(f"Optimization failed: {str(e)}")
            raise

    def _evaluate_strategy(self, strategy: Dict) -> Dict:
        """
        Evaluates a single strategy based on predefined criteria.
        """
        evaluation = {
            'score': 0,
            'valid': False
        }
        
        # Basic checks
        if not strategy.get('id'):
            return evaluation
            
        # Evaluate against business goals (example)
        if self._meets_risk_tolerance(strategy):
            evaluation['score'] += 50
        
        return evaluation
    
    def _meets_risk_tolerance(self, strategy: Dict) -> bool:
        """
        Checks if the strategy adheres to risk tolerance.
        """
        risk = strategy.get('risk_level', 0)
        return risk <= Settings.RISK_TOLERANCE

# Initialize optimizer instance
optimizer_instance = FinancialStrategyOptimizer()