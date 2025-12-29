from core.evaluator import Evaluator
from core.scoring import ScoreCalculator
import json
import datetime

class AttackEngine:
    def __init__(self, model, challenge_id):
        self.model = model
        self.challenge_id = challenge_id
        self.attempts = 0

    def log_attack(self, prompt, response, success):
        log_entry = {
            "timestamp": str(datetime.datetime.now()),
            "challenge": self.challenge_id,
            "prompt": prompt,
            "response": response,
            "success": success
        }

        try:
            with open("logs/attacks.json", "r+") as f:
                data = json.load(f)
                data.append(log_entry)
                f.seek(0)
                json.dump(data, f, indent=2)
        except:
            with open("logs/attacks.json", "w") as f:
                json.dump([log_entry], f, indent=2)

    def run(self):
        print("\nType 'exit' to quit\n")

        while True:
            user_prompt = input("You: ")
            if user_prompt.lower() == "exit":
                break

            self.attempts += 1
            response = self.model.send(user_prompt)

            print("\nModel:", response)

            success = Evaluator.evaluate(self.challenge_id, response)
            self.log_attack(user_prompt, response, success)

            if success:
                score = ScoreCalculator.calculate(self.attempts, True)
                print(f"\n🔥 ATTACK SUCCESSFUL")
                print(f"✔ Attempts: {self.attempts}")
                print(f"🏆 Score: {score}")
                break
