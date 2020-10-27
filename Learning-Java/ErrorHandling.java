
public class ErrorHandling {
	/*
	 * Types of Error:
	 * Syntax Error -> Incorrect syntax which would usually cause an error to be thrown
	 * Logic Error -> Usually does not cause an error to be thrown aka syntax correct but the output is still incorrect
	 */
	public static void main(String[] args) {
		try {
			int[] arr = {1,2,3};
			
			/*since arrays start with index 0 this means index 3 does not exists which
				should throw IndexOutOfBoundsException*/
			System.out.print(arr[3]);
		/*It is generally better to use specific exception so that it makes debugging easier 
		but for this case Exception works as well since we already know what error it would throw*/
		}catch(Exception err) {
			err.printStackTrace();
			//System.out.println(err.getMessage());
		}
		/*this is usually used to perform something that must be done regardless if the code
		throws an exception or not. e.g. closing inputstream, etc*/
		finally {
			
		}
	}
}
