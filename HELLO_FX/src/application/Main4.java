package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main4 extends Application {
	
	TextField tf ;
	Label lable ;
	Button btn ;
	
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main4.fxml"));
			Scene scene = new Scene(root,200,200);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tf = (TextField) scene.lookup("#tf");
			lable = (Label) scene.lookup("#result");
			btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick();
				}
			});
			tf.setOnKeyPressed(new EventHandler<KeyEvent>() {
		        @Override
		        public void handle(KeyEvent kEvent) {
		        	if (kEvent.getCode().equals(KeyCode.ENTER)) {
		                myClick();
		            }
		        }
			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	public void myClick() {
		String user = "";
		String com = "";
		String result = "";
		user = tf.getText();
		double rnd = Math.random();
		
		if(rnd > 0.5) {
			com = "홀";
		} else {
			com = "짝";
		}
		
		result += "컴퓨터: " + com;
		result += "\n";
		result += "나: " + user;
		result += "\n" + "결과: ";
		
		if(user.equals(com)) {
			result += "이겼습니다.";
		} else {
			result += "졌습니다.";
		}
		
		lable.setText(result);
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
