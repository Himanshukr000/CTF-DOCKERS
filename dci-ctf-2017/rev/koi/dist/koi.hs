import Data.Eq
import Control.Monad
import System.IO

data S a = S a

instance Functor S where
  fmap f (S x) = S (f x)

instance Applicative S where
  pure = S
  (S f) <*> (S x) = S (f x)

instance Monad S where
  (S x) >>= f = f x

koi :: String -> S Int -> Bool
koi ('s':xs) s@(S 5) = koi xs.fmap(flip div 5)$s
koi ('m':xs) s@(S 9) = koi xs$(S 5)>>(S 6)>>(S 7)>>(S 8)>>(S 9)>>(S 10)
koi ('S':xs) s@(S 1) = koi xs$do{x<-s;pure(x+2)}
koi ('u':xs) s@(S 6) = koi xs.fmap(+(maybe 1 undefined Nothing))$s
koi ('i':xs) s@(S 4) = koi xs$s>>=(return.(+ 1))
koi ('#':xs) s@(S 1) = koi xs.(<$>)id$s
koi ('u':xs) s@(S 3) = koi xs$pure(.)`ap`S(flip div 3)<*>S(*4)<*>s
koi ('t':xs) s@(S 11) = koi xs$iterate((<$>)(flip(-)1))s!!4
koi ('e':xs) s@(S 2) = koi xs.fmap(flip div 2)$s
koi ('t':xs) s@(S 7) = koi xs$(*2)<$>(*2)<$>(flip(-)5)<$>s
koi ('o':xs) s@(S 8) = koi xs.fmap (+1)$s
koi ('e':xs) s@(S 7) = not$koi "???"$return$1234
koi ('J':xs) s@(S 1) = koi xs$(<$>)(flip div 2).fmap (+3) $ s
koi ('A':xs) s@(S 1) = koi xs$pure(.)<*>S(*(length$takeWhile(<3)[1..]))<*>S(*(gcd 21 12))<*>s
koi ('a':xs) s@(S 10) = koi xs$s>>=(pure.foldr(.)(*2)[(flip(-)9)])
koi _ _ = False

main = do hSetBuffering stdout NoBuffering
          putStr "Enter key: "
          line <- getLine
          if koi line (return 1) && length line == 15 then
            putStrLn $ concat ["DCI{", line, "}"]
          else
            putStrLn "Bad key"
