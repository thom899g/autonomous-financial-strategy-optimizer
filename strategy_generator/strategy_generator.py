from typing import Dict, List
import pandas as pd

class StrategyGenerator:
    def __init__(self):
        pass
        
    def generate(self, strategies_data: Dict) -> List[Dict]:
        """
        Generates financial strategies based on market data.
        """
        try:
            # Example: Generate moving average crossover strategies
            df = pd.DataFrame(strategies_data)
            strategies = []
            
            for symbol in df['symbol'].unique():
                strategy = self._generate_moving_average_strategy(symbol, df[df['symbol'] == symbol])
                if strategy:
                    strategies.append(strategy)
                    
            return strategies
            
        except Exception as e:
            raise ValueError(f"Failed to generate strategies: {str(e)}")
            
    def _generate_moving_average_strategy(self, symbol: str, data: pd.DataFrame) -> Dict:
        """
        Generates a moving average crossover strategy for a given symbol.
        """
        if len(data) < 50:
            return None
            
        # Simplified strategy generation
        short_ma = data['close'].rolling(10).mean()
        long_ma = data['close'].rolling(20).mean()
        
        entry_points = (short_ma > long_ma).idxmax()
        exit_points = (short_ma < long_ma).idxmax()
        
        return {
            'id': f"MA_{symbol}_strategy",
            'symbol': symbol,
            'entry_points': [entry_points],
            'exit_points': [exit_points],
            'risk_level': self._calculate_strategy_risk(entry_points, exit_points)
        }
    
    def _calculate_strategy_risk(self, entry: int, exit: int) -> float:
        """
        Calculates the risk level of a strategy based on hold time.
        """
        duration = exit - entry
        return min(duration / 10, 0.5)  # Simplified model