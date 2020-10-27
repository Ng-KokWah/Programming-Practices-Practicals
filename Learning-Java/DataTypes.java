
public class DataTypes {
	public static void main(String[] args) {
		/*
		 * byte	1 byte	Stores whole numbers from -128 to 127
		 * short	2 bytes	Stores whole numbers from -32,768 to 32,767
		 * int	4 bytes	Stores whole numbers from -2,147,483,648 to 2,147,483,647
		 * long	8 bytes	Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
		 * float	4 bytes	Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits
		 * double	8 bytes	Stores fractional numbers. Sufficient for storing 15 decimal digits
		 * boolean	1 bit	Stores true or false values
		 * char	2 bytes	Stores a single character/letter or ASCII values
		 * 
		 * Primitive types are predefined (already defined) in Java. Non-primitive types are created by the programmer and is not defined by Java (except for String).
		 * Non-primitive types can be used to call methods to perform certain operations, while primitive types cannot.
		 * A primitive type has always a value, while non-primitive types can be null.
		 * A primitive type starts with a lowercase letter, while non-primitive types starts with an uppercase letter.
		 * The size of a primitive type depends on the data type, while non-primitive types have all the same size.
		 */
		
		/*
		 * NOTE:
		 * 1. division by 0 is not possible
		 * 2. when anything that is stored as a string is added to any other variables, concatenation occurs
		 * e.g. int num1 = 5
		 * String num2 = "7"
		 * num1 + num2 = 57
		 * 3. when trying to concatenate 2 integers, add a "" between to prevent it from adding together
		 */
		
		int myNum = 5;
		double myDouble = 2.32;
		float myFloatNum = 5.99f;
		char myLetter = 'D';
		boolean myBool = true;
		String myText = "Hello";
	}
}
