{-# LANGUAGE TypeApplications #-}
module Main where

import Data.List

-- example of lazy fibonacci numbers list
-- fibs :: [Integer]
-- fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

main = do
    xs <- do
        xs <- sort . map read . lines <$> readFile "./10.in"
        return $ [0] ++ xs ++ [last xs + 3]
    let dp = 1 : map (\x -> 
                        sum $ 
                        map snd $ 
                        takeWhile (\(y, _) -> y < x) $ 
                        dropWhile (\(y,_) -> x - y > 3) $ 
                        zip xs dp)
                     (tail xs)
    print $ last dp -- 64793042714624

