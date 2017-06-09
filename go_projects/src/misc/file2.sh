#http://www.dailyfreecode.com/code/shell-convert-contents-uppercase-1635.aspx
clear
<<"COMMENT"
echo "Hello World"
echo "Hello ${LOGNAME}"  # Accessing system variable
echo "$(date)"		# Accessing command
echo "Hello World Last line"
COMMENT


<<"COMMENT"
echo "Multi line comment working now"
echo "UserName = : ${USERNAME}" # Gives null/empty String
echo "Home = : ${HOME}"
echo "Home = : ${LOGNAME}"
COMMENT

<<"COMMENT"
echo "Today'S date [using back quotes] :=  `date`" # This is not single quote, see tilde btn.
expr 1 + 3
echo $?
COMMENT



<<"COMMENT"
#How to read command line arguments. See below

echo "Total no. of command line arguments are $#" # 2
echo "$0 is script name" 			# ./file2.sh is script name
echo "$1 is first argument" 			#hello is first argument
echo "$2 is second argument" 			# world is second argument
echo "All of them are :- $*" 			# All of them are :- hello world

# If we put at command line --> hello sinha ./file2.sh 
#COMMENT



<<"COMMENT"
# Exit Status [$?]

expr 20 + 5  # Space is must 
echo $?  # 0 indicates, successfully executed
COMMENT



<<"COMMENT"
# If then fi Command

if cat $1
  then  echo -e "\n\n File $1, found and echoed" # -e put 1 blank line
fi

# If we  put following command --> ./file2.sh testFile
COMMENT




<<"COMMENT"

# Test expr
if test $1 -gt 5 -a $1 -lt 10 		# given no must be > 5 AND < 10
 then echo "if part executed... $1 number is > 5 & less than 10 "

else
 echo "else part eecuted. Check $1 is > 5 AND < 10"
fi

COMMENT


<<"COMMENT"
# String comparison

compName="cantata"
echo "$compName" 	# Don't put any space

if test $1 = "$compName"
  then  echo  "if part i.e cantata executed."
else
  echo "You not given Cantata"
fi


COMMENT


<<"COMMENT"
# String case conversion & Length
# http://www.linuxnix.com/shell-scripting-convert-a-string-from-
#lowercase-to-uppercase/
# http://landoflinux.com/linux_bash_scripting_substring_tests.html

name="surendra kumar"

name_upr=${name^^} # Converted into upper case
echo $name_upr 

name_lwr=${name,,} # Converted into lower case
echo $name_lwr 
echo "Our variable $name is ${#name} characters long" # Length here
COMMENT

#Extracting a Substring from a Variable
#http://landoflinux.com/linux_bash_scripting_substring_tests.html


<<"COMMENT"
test="Welcome to the Land of Linux"
echo "Our variable test is ${#test} characters long"
strLen=${#test} #  dbl Quotes also vallid "${#test}"
echo "------ Total length of given string = : $strLen" #---------------

test1=${test:0:7}
test2=${test:15:13}
test3=${test:0}
echo "test = : " $test
echo "test1 (0 to 7) = : " $test1
echo "test2 (15 : 13)= : " $test2
echo "test3 (0) = : " $test3



COMMENT
