package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main7 extends Application {
	TextField tf1;
	TextField tf2;
	TextField tf3;

	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main7.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			tf3 = (TextField) scene.lookup("#tf3");

			Button btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					goGame();
				}
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	public void goGame() {
		String mine = tf1.getText();
		String com = "";
		String result = "";
		String[] arr = {"가위", "바위", "보"};
		int rnd = (int) (Math.random()*3);
		com = arr[rnd];
		
		if(mine.equals("가위") && com.equals("바위")) {result = "컴퓨터 승리!";}
		if(mine.equals("가위") && com.equals("보")) {result = "나 승리!";}
		if(mine.equals("가위") && com.equals("가위")) {result = "비김!";}
		
		if(mine.equals("바위") && com.equals("바위")) {result = "비김!";}
		if(mine.equals("바위") && com.equals("보")) {result = "컴퓨터 승리!";}
		if(mine.equals("바위") && com.equals("가위")) {result = "나 승리!";}
		
		if(mine.equals("보") && com.equals("바위")) {result = "나 승리!";}
		if(mine.equals("보") && com.equals("보")) {result = "비김!";}
		if(mine.equals("보") && com.equals("가위")) {result = "컴퓨터 승리!";}

		
		tf2.setText(com);
		tf3.setText(result);
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
