package test;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.PageFactory;
import org.testng.annotations.Test;

public class EmailClickDemo {

	@Test
	public void clickEmail() {

		String driverPath = System.getProperty("user.dir");
		System.setProperty("webdriver.chrome.driver", driverPath + "\\drivers\\chromedriver.exe");
		ChromeDriver driver = new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("https://mail.google.com");
		GmailPageObjects gp=PageFactory.initElements(driver, GmailPageObjects.class);
		gp.enterEmail("<YOUR_EMAIL_ID>");//Replace with your email id
		gp.enterPassword("<PASSWORD>");//Replace with your password
		gp.clickEmail("<EMAIL SUBJECT YOU WANT TO CLICK>");//Replace with email subject you want to click
		
		
	}

	

	
}
