package day02;

public class OopTest {
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println(ani.myLife);
		ani.getAge();
		System.out.println(ani.myLife);
		
		Human person = new Human();
		System.out.println(person.skillLang);
		person.getAge();
		person.exp(50);
		System.out.println(person.myLife);
		System.out.println(person.skillLang);
		
	}
}
