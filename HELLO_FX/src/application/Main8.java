package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main8 extends Application {
	TextField tf1;
	TextField tf2;
	TextArea ta;

	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main8.fxml"));
			Scene scene = new Scene(root,300,300);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			ta = (TextArea) scene.lookup("#ta");

			Button btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					showStar();
				}
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	public void showStar() {
		String firstVal = tf1.getText();
		String endVal = tf2.getText();
		int startNum = Integer.parseInt(firstVal);
		int endNum = Integer.parseInt(endVal);
		
		String text = "";
		
		for(int i = startNum; i<=endNum; i++) {
			text += drowStar(i);
		}
		
		
		ta.setText(text);
		
	}
	
	public String drowStar(int cnt) {
		String ret = "";
		
		for(int i=0; i<cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
