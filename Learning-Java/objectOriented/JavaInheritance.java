package objectOriented;

/*
 * inheritance helps to 
 * improve code reusability
 * reduce repetition in terms of attributes and methods
 * since it allows one class to inherit the attributes and method from another class
 * 
 * superclass (parent) - the class being inherited from
 * subclass (child) - the class that inherits from another class
 * 
 * Obviously the class you attempt to inherit from must not be declared final and cannot have access modifier of private
 */
class Vehicle {
	protected String brand = "Ford";        // Vehicle attribute
	public void honk() {                    // Vehicle method
		System.out.println("Tuut, tuut!");
	}
}

public class JavaInheritance extends Vehicle {
	private String modelName = "Mustang";    // Car attribute
	  public static void main(String[] args) {

	    // Create a myCar object
	    JavaInheritance myCar = new JavaInheritance();

	    // Call the honk() method (from the Vehicle class) on the myCar object
	    myCar.honk();

	    // Display the value of the brand attribute (from the Vehicle class) and the value of the modelName from the Car class
	    System.out.println(myCar.brand + " " + myCar.modelName);
	  }
}
