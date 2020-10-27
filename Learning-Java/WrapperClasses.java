
public class WrapperClasses {
	/*
	 * Primitive Data Type	Wrapper Class
	 * byte					Byte
	 * short				Short
	 * int					Integer
	 * long					Long
	 * float				Float
	 * double				Double
	 * boolean				Boolean
	 * char					Character
	 * 
	 * in some cases like working with collection objects
	 * like arraylist you can only use the wrapper class
	 * 
	 * ArrayList<int> myNumbers = new ArrayList<int>(); // Invalid
	 * ArrayList<Integer> myNumbers = new ArrayList<Integer>(); // Valid
	 */
	public static void main(String[] args) {
		Integer myInt = 5;
	    Double myDouble = 5.99;
	    Character myChar = 'A';
	    
	    //you can still get the values of the variables normally like myInt
	    //but using the wrapper class gives the option of using datatypeValue() 
	    //to get the values of the variables when using a wrapper class
	    System.out.println(myInt.intValue());
	    System.out.println(myDouble.doubleValue());
	    System.out.println(myChar.charValue());
	    
	    //it also gives a useful method of .length and .toString()
	    String myString = myInt.toString();
	    System.out.println(myString.length());
	}
}
