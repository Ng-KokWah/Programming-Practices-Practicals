
public class TypeCasting {
	 public static void main(String[] args) {
		 	//Widening Casting -> passing smaller size data type to a larger size data type
		    int myInt = 9;
		    double myDouble = myInt; // Automatic casting: int to double

		    System.out.println(myInt);      // Outputs 9
		    System.out.println(myDouble);   // Outputs 9.0
		    
		    //Narrowing Casting -> must be done manually
		    double myDouble2 = 9.78;
		    int myInt2 = (int) myDouble2; // Manual casting: double to int

		    System.out.println(myDouble2);   // Outputs 9.78
		    System.out.println(myInt2);      // Outputs 9
	 }
}
