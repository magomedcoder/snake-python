class Score:

    def get(self):
        high_score = 0
        try:
            high_score_file = open("../score.txt", "r")
            high_score = int(high_score_file.read())
            high_score_file.close()
        except IOError:
            print("Высоких баллов нет.")
        except ValueError:
            print("Начать не с высоких баллов")
        return high_score

    def save(self):
        try:
            high_score_file = open("../score.txt", "w")
            high_score_file.write(str(self))
            high_score_file.close()
        except IOError:
            print("Не удалось сохранить.")
