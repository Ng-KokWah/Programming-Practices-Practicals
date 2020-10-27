import java.util.Scanner;

public class UserInputScanner {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String name = sc.nextLine();
		System.out.println("Enter your name: ");
		
		System.out.println("Hello, " + name);
		sc.close();
	}
}
