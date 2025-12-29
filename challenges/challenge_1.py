class ScoreCalculator:
    @staticmethod
    def calculate(attempts: int, success: bool) -> int:
        if not success:
            return 0
        base = 100
        penalty = attempts * 10
        return max(base - penalty, 10)
