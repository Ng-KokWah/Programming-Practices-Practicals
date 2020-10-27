package objectOriented;

/*
 * Polymorphism means "many forms", and it occurs when we have many classes that 
 * are related to each other by inheritance. 
 * 
 * Inheritance lets us inherit attributes and methods while polymorphism uses those methods to perform
 * different tasks, allowing you to perform a single action in different ways
 * 
 * Why use it?
 * it is for code reusability, allows you to reuse methods in existing class when you create new classes
 */

class Animal {
	  public void animalSound() {
	    System.out.println("The animal makes a sound");
	  }
	}

	class Pig extends Animal {
	  public void animalSound() {
	    System.out.println("The pig says: wee wee");
	  }
	}

	class Dog extends Animal {
	  public void animalSound() {
	    System.out.println("The dog says: bow wow");
	  }
}
	
public class JavaPolymorphism {
	public static void main(String[] args) {
		Animal myAnimal = new Animal();  // Create a Animal object
	    Animal myPig = new Pig();  // Create a Pig object
	    Animal myDog = new Dog();  // Create a Dog object
	    myAnimal.animalSound();
	    myPig.animalSound();
	    myDog.animalSound();
	}
}
