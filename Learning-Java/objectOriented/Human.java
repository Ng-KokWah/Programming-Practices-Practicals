package objectOriented;
/*
 * USED in JavaEncapsulation.java file
 * 
 * this file also has sample of a constructor
 * A constructor is a special method used to initialize objects
 * the constructor is called when an object of a class is created that sets
 * the initial values for object attributes/variables
 * 
 * you can either have 1 constructor or have multiple constructors
 * though if you have multiple constructors, they need to 
 * be different in terms of the parameters it takes
 * 
 * though by default a constructor is create by java if you do not specify
 */
public class Human {
	private String name; // private = restricted access
	private int age;
	
	//1st constructor, since you already created a constructor, the default Human()
	//constructor is no longer automatically created by java
	public Human() {
		
	}

	//2nd constructor
	public Human(String name) {
		this.name = name;
	}
	
	//3rd constructor
	public Human(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}
	// Getter
	public String getName() {
	  return name;
	}

	// Setter
	public void setName(String newName) {
	  this.name = newName;
	}
}
