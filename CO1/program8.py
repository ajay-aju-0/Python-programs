# Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.[eg: onion -> oni$n]

main_string = input("Type a string : ")
char = main_string[0]
main_string = main_string.replace(char,'$')
print(char+main_string[1:])

# method2
# word1=str(input("enter a word:"))
# word2=word1
# new=word2[0]
# word2=word2.replace(new,"$")
# word2=new+word2[1:]
# print(word2)