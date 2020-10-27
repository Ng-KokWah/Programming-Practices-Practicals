
public class Operators {
	public static void main(String[] args) {
		//Arithmetic Operators
		int add = 3 + 4;
		int minus = 5 - 3;
		int divide = 15 / 5;
		int multiply = 10 * 4;
		int mod = 10 % 5;
		
		System.out.println("Add:" + add + "\nMinus: " + minus + "\nDivide: " + divide + "\nMultiply: " + multiply + "\nModulus: " + mod);
		
		int num = 5;
		System.out.println(num++); //still 5 executes after this statement
		int num2 = 5;
		System.out.println(++num2); //6 since it executes in this statement itself
		
		int num3 = 5;
		System.out.println(num3--); //still 5 executes after this statement
		int num4 = 5;
		System.out.println(--num4); //4 since it executes in this statement itself
		
		//Assignment Operators
		int a = 10;
		System.out.println(a += 10); //20
		
		//Comparison Operators
		int b = 50;
		//!= not equals, > greater than, < less than, >= greater than or equal to, <= less than or equal to
		if(b == 50) {
			System.out.println("Yes");
		}
		
		//Logical Operators
		//&& both conditions must match, || either condition match can already, ! reverse the statement
		if(b > 0 && b <=50) {
			System.out.println("Pass");
		}
	}
}
