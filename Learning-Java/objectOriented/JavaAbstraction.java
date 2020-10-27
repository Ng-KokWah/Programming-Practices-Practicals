package objectOriented;

/*
 * Data abstraction is the process of hiding certain details and showing
 * only essential information to the user
 * 
 * abstraction can be achieved with either abstract class or interfaces
 * 
 * abstract is a non-access modifier:
 * abstract class -> restricted class that cannot be used to create objects
 * (to access it, you must inherit from another class)
 * 
 * abstract method -> can only be used in an abstract class, and it does not have a body.
 * The body is provided by the subclass (inherited from)
 * 
 * Why use it?
 * to achieve security by hiding details and showing only what is essential
 */

//METHOD 1: Abstract class
abstract class Animals {
	// Abstract method (does not have a body)
	public abstract void animalSound();
	// Regular method
	public void sleep() {
		System.out.println("Zzz");
	}
}

//Subclass (inherit from Animal)
class Pigs extends Animals {
	public void animalSound() {
		// The body of animalSound() is provided here
		System.out.println("The pig says: wee wee");
	}
}

//METHOD 2: Interface -> is a completely abstract class that is used to 
//group related methods with empty bodies
interface FirstInterface {
	public void myMethod(); // interface method
}

interface SecondInterface {
	public void myOtherMethod(); // interface method
}

class DemoClass implements FirstInterface, SecondInterface {
	  public void myMethod() {
	    System.out.println("Some text..");
	  }
	  public void myOtherMethod() {
	    System.out.println("Some other text...");
	  }
}

public class JavaAbstraction {
	public static void main(String[] args) {
		Pigs myPig = new Pigs(); // Create a Pig object
	    myPig.animalSound();
	    myPig.sleep();
	    
	    //for the interfaces
	    DemoClass demo = new DemoClass();
	    demo.myMethod();
	    demo.myOtherMethod();
	}
}
