
/*
 * this is also known as to nest classes, so as to group classes that belong together
 */
class OuterClass {
  int x = 10;
  
  //if you declare this as static you would be able to acces it by 
  //OuterClass.InnerClass inner = new OuterClass.InnerClass();
  //SOP(inner.y);
  class InnerClass {
	int y = 9;
	
    public int myInnerMethod() {
      return x;
    }
  }
}

public class InnerClasses {
	public static void main(String[] args) {
		//since the inner class is not static you need to create an object of outerclass first
		 OuterClass myOuter = new OuterClass();
		 OuterClass.InnerClass myInner = myOuter.new InnerClass();
		 System.out.println(myInner.myInnerMethod());
	}
}
