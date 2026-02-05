class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x=0
        y=0
        cows=[]
        bulls=list(guess)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                x+=1
                bulls.remove(guess[i])
            else:
                cows.append(secret[i])
        for i in cows:
            if i in bulls:
                y+=1
                bulls.remove(i)
        result=str(f'{x}A{y}B')
        return result

    

        