
public class Conditions {

	public static void main(String[] args) {
		int results = 1000;
		
		String passOrFail = "";
		if(results >= 50 && results <= 100) {
			passOrFail = "Passed";
		}
		else if(results >= 0 && results < 50) {
			passOrFail = "Failed";
		}
		else {
			passOrFail = "Invalid Result";
		}
		
		System.out.println(passOrFail);
		
		//using a ternary operator -> variable = (condition) ? expressionTrue :  expressionFalse;
		passOrFail = (results >= 50 && results <= 100) ? "Passed" : "Failed";
		System.out.println(passOrFail);
	}

}
