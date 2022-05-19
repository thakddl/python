package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main6 extends Application {
	Label lbl;
	TextField tf;
	TextArea ta;
	String inputDan;
	int dan;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main6.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			lbl = (Label) scene.lookup("#lbl");
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");

			Button btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					getGugu();
				}
			});
			tf.setOnKeyPressed(new EventHandler<KeyEvent>() {
				@Override
				public void handle(KeyEvent event) {
					if(event.getCode().equals(KeyCode.ENTER)) {						
						getGugu();
					}
					
				}
				
			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	public void getGugu() {
		inputDan = tf.getText();
		dan = Integer.parseInt(inputDan);
		String text = "";
		text += dan + " * " + 1 + " = " + (dan * 1) + "\n";
		text += dan + " * " + 2 + " = " + (dan * 2) + "\n";
		text += dan + " * " + 3 + " = " + (dan * 3) + "\n";
		text += dan + " * " + 4 + " = " + (dan * 4) + "\n";
		text += dan + " * " + 5 + " = " + (dan * 5) + "\n";
		text += dan + " * " + 6 + " = " + (dan * 6) + "\n";
		text += dan + " * " + 7 + " = " + (dan * 7) + "\n";
		text += dan + " * " + 8 + " = " + (dan * 8) + "\n";
		text += dan + " * " + 9 + " = " + (dan * 9) + "\n";
		
		ta.setText(text);
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
