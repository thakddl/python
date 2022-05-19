package application;
	
import java.util.Timer;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main10 extends Application {
	Label lbl;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main10.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			lbl = (Label) scene.lookup("#lbl");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					Timer tm = new Timer();
					startTimer();
				}
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	public void startTimer() {
		Thread th = new Thread(new Runnable() {
			String tmVal = lbl.getText();
			int startTm = Integer.parseInt(tmVal);
			int sec;
			@Override
			public void run() {
				for(sec=startTm; sec<=10; sec++) {
					Platform.runLater(()->{					
						lbl.setText(sec+"");
					});
					try {
						Thread.sleep(1000);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		});
		th.start();
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
