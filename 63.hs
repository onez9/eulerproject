import Data.Function ((&))

answer = allAnswers & takeWhile (not.null) & concat & length

allAnswers = map getAllNDigitNthPower [1..]

getAllNDigitNthPower n =
        nthPowers n & getNDigitNums n

-- monotonically increasing ms
getNDigitNums n [] = []
getNDigitNums n (m:ms)
        | numDigits m < n = getNDigitNums n ms
        | numDigits m == n = m : getNDigitNums n ms
        | otherwise = [] 

numDigits n =
        length $ show n

nthPowers n = map (^n) [1..]

main = print answer