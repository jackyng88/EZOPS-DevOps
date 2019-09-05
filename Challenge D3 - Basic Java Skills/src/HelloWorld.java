
public class HelloWorld {
	
	static void throwExceptionExample(String input) {
		if (input != "Hello world!") {
			throw new IllegalArgumentException("You didn't say hello world properly!");
		}
		System.out.println(input);
		
	}

	public static void main(String[] args) {
		
		try {
			//System.out.println("Hello world!");
			String helloWorld = "Hello world!";
			String exceptionString = "Hello earth!";
			throwExceptionExample(exceptionString);
		}
		
		catch(IllegalArgumentException E) {
			//System.out.println(E);
			//E.getMessage();
			E.printStackTrace();
		}
	}

}
