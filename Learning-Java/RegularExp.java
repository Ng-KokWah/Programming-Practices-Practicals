import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
 * a regular expression uses a search pattern to find something
 * 
 * Pattern - defines the pattern
 * Matcher - used to search for the pattern
 * PatternSyntaxException - indicates syntax error in a regex pattern
 * 
 * Regex
 * [abc]	Find one character from the options between the brackets
 * [^abc]	Find one character NOT between the brackets
 * [0-9]	Find one character from the range 0 to 9
 * 
 * Metacharacters -> characters with special meanings
 * |	Find a match for any one of the patterns separated by | as in: cat|dog|fish
 * .	Find just one instance of any character
 * ^	Finds a match as the beginning of a string as in: ^Hello
 * $	Finds a match at the end of the string as in: World$
 * d	Find a digit
 * \s	Find a whitespace character
 * \b	Find a match at the beginning of a word like this: \bWORD, or at the end of a word like this: WORD\b
 * \u1234	Find the Unicode character specified by the hexadecimal number xxxx
 * 
 * Quantifiers -> specify match how many times
 * n+	Matches any string that contains at least one n
 * n*	Matches any string that contains zero or more occurrences of n
 * n?	Matches any string that contains zero or one occurrences of n
 * n{x}	Matches any string that contains a sequence of X n's
 * n{x,y}	Matches any string that contains a sequence of X to Y n's
 * n{x,}	Matches any string that contains a sequence of at least X n's
 */
public class RegularExp {
	public static void main(String[] args) {
		/*
		 * the compile has a few available flags like
		 * Pattern.CASE_INSENSITIVE - The case of letters will be ignored when performing a search.
		 * Pattern.LITERAL - Special characters in the pattern will not have any special meaning and will be treated as ordinary characters when performing a search.
		 * Pattern.UNICODE_CASE - Use it together with the CASE_INSENSITIVE flag to also ignore the case of letters outside of the English alphabet
		 */
		Pattern pattern = Pattern.compile("test", Pattern.CASE_INSENSITIVE);
		Matcher matcher = pattern.matcher("This is a test");
		boolean matchFound = matcher.find();
		if(matchFound) {
			System.out.println("Found!");
		}
		else {
			System.out.println("Not Found");
		}
	}
}
