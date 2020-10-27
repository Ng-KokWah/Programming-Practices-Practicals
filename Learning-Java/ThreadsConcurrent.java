
/*
 * Threads allows programs to be more efficient by doing
 * multiple things at the same time
 * 
 * Threads can perform compilcated tasks in the background without 
 * interrupting the main program
 */
//Two methods to implement threads
// one is to use extends Thread or the other is implements Runnable
//The main difference is when you extend Thread you cannot extend any other classes
// but by implements Runnable interface you can still extend from other classes
public class ThreadsConcurrent extends Thread {
	public static void main(String[] args) {
		//to run a thread when using extends Thread
		ThreadsConcurrent thread = new ThreadsConcurrent();
	    thread.start();
	    System.out.println("This code is outside of the thread");
	    // to run a thread when using implements Runnable
	    /*ThreadsConcurrent obj = new ThreadsConcurrent();
	    Thread threads = new Thread(obj);
	    threads.start();
	    System.out.println("This code is outside of the thread");
	    */
	    
	    /*
	     * Because threads run at the same time as other parts of the program, 
	     * there is no way to know in which order the code will run. 
	     * When the threads and main program are reading and writing the same variables, 
	     * the values are unpredictable. 
	     * The problems that result from this are called concurrency problems.
	     * 
	     * To solve this concurrency issue
	     * 1. share as few attributes(variables) between thread as possible
	     * 2. if attributes are shared, Use isAlive() to check if the thread
	     * e.g. 
	     *  while(thread.isAlive()) {
	     *  	System.out.println("Waiting...");
	     *   }
	     */
	}
	
	public void run() {
	    System.out.println("This code is running in a thread");
	  }
}
