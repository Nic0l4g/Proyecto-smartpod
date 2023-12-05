package com.example.gymapp;

import static com.example.gymapp.R.color.purple_500;

import android.annotation.SuppressLint;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.content.res.ColorStateList;
import android.graphics.Color;
import android.graphics.drawable.ClipDrawable;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.Drawable;
import android.os.Build;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.content.res.ColorStateList;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;
import androidx.core.content.ContextCompat;


public class ViewPlant extends AppCompatActivity {
    private Button buttonBack;
    TextView tv_texto;
    TextView th_texto;
    TextView luz_txt;
    TextView ts_txt;
    private DatabaseReference mDatabase;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_plant);



        buttonBack = findViewById(R.id.buttonBack);

        buttonBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish(); // Cierra la actividad actual y regresa a la actividad anterior
            }
        });


        tv_texto = (TextView) findViewById(R.id.tv_texto);
        th_texto = (TextView) findViewById(R.id.th_texto);
        luz_txt = (TextView) findViewById(R.id.luz_txt);
        ts_txt = (TextView) findViewById(R.id.ts_txt);
        mDatabase = FirebaseDatabase.getInstance().getReference();

        mDatabase.child("last_data").addValueEventListener(new ValueEventListener() {
            @SuppressLint("ResourceAsColor")
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                if (dataSnapshot.exists()) {

                    int t = Integer.parseInt(dataSnapshot.child("temperature").getValue().toString());

                    // Convertir int a String antes de establecerlo en el TextView
                    tv_texto.setText(String.valueOf(t));

                    ProgressBar progressBar = findViewById(R.id.pb_t);

                    // Calcula el progreso relativo dentro de los umbrales
                    int progress;
                    if (t <= 10) {
                        sendNotification("Planta en peligro", "La temperatura es baja. ¡La planta está en peligro!");

                        progress = 10;
                    } else if (t > 10 && t <= 15) {
                        progress = 50;
                    } else {

                        progress = 100;
                    }

                    // Crea un Drawable con el color especificado
                    int color;
                    if (t <= 10) {
                        color = Color.parseColor("#FF0000"); // Rojo para temperaturas bajas
                    } else if (t > 10 && t <= 15) {
                        color = Color.parseColor("#FFFF00"); // Amarillo para temperaturas medias
                    } else {
                        color = Color.parseColor("#00FF00"); // Verde para temperaturas altas
                    }

                    Drawable progressDrawable = new ClipDrawable(new ColorDrawable(color), Gravity.START, ClipDrawable.HORIZONTAL);

                    // Establece el Drawable personalizado en la ProgressBar
                    progressBar.setProgressDrawable(progressDrawable);

                    // Establece el progreso en la ProgressBar
                    progressBar.setProgress(progress);

                } else {
                    // Manejar el caso en el que los datos no existen
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                // Manejar errores de la base de datos
            }
        });







        mDatabase.child("last_data").addValueEventListener(new ValueEventListener() {
            @SuppressLint("ResourceAsColor")
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                if (dataSnapshot.exists()) {

                    int ha = Integer.parseInt(dataSnapshot.child("humidity ambient").getValue().toString());

                    // Convertir int a String antes de establecerlo en el TextView
                    th_texto.setText(String.valueOf(ha));

                    ProgressBar progressBar = findViewById(R.id.pb_ha);

                    // Calcula el progreso relativo dentro de los umbrales
                    int progress;
                    if (ha <= 30) {
                        sendNotification("Planta en peligro", "La humedad del ambiente es baja. ¡La planta está en peligro!");
                        progress = 10;
                    } else if (ha > 30 && ha <= 40) {
                        progress = 50;
                    } else {
                        progress = 100;
                    }

                    // Crea un Drawable con el color especificado
                    int color;
                    if (ha <= 30) {
                        color = Color.parseColor("#FF0000"); // Rojo para humedad baja
                    } else if (ha > 30 && ha <= 40) {
                        color = Color.parseColor("#FFFF00"); // Amarillo para humedad media
                    } else {
                        color = Color.parseColor("#00FF00"); // Verde para humedad alta
                    }

                    Drawable progressDrawable = new ClipDrawable(new ColorDrawable(color), Gravity.START, ClipDrawable.HORIZONTAL);

                    // Establece el Drawable personalizado en la ProgressBar
                    progressBar.setProgressDrawable(progressDrawable);

                    // Establece el progreso en la ProgressBar
                    progressBar.setProgress(progress);

                } else {
                    // Manejar el caso en el que los datos no existen
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                // Manejar errores de la base de datos
            }
        });






        mDatabase.child("last_data").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                if (dataSnapshot.exists()) {

                    int hs = Integer.parseInt(dataSnapshot.child("humidity soil").getValue().toString());

                    // Convertir int a String antes de establecerlo en el TextView
                    ts_txt.setText(String.valueOf(hs));

                    ProgressBar progressBar = findViewById(R.id.pb_hs);

                    // Calcula el progreso relativo dentro de los umbrales
                    int progress;
                    if (hs <= 30) {
                        progress = 10;
                        sendNotification("Planta en peligro", "La humedad del suelo es baja. ¡La planta está en peligro!");

                    } else if (hs > 30 && hs <= 40) {
                        progress = 50;
                    } else {
                        progress = 100;
                    }

                    // Crea un Drawable con el color especificado
                    int color;
                    if (hs <= 30) {
                        color = Color.parseColor("#FF0000"); // Rojo para humedad del suelo baja
                    } else if (hs > 30 && hs <= 40) {
                        color = Color.parseColor("#FFFF00"); // Amarillo para humedad del suelo media
                    } else {
                        color = Color.parseColor("#00FF00"); // Verde para humedad del suelo alta
                    }

                    Drawable progressDrawable = new ClipDrawable(new ColorDrawable(color), Gravity.START, ClipDrawable.HORIZONTAL);

                    // Establece el Drawable personalizado en la ProgressBar
                    progressBar.setProgressDrawable(progressDrawable);

                    // Establece el progreso en la ProgressBar
                    progressBar.setProgress(progress);

                } else {
                    // Manejar el caso en el que los datos no existen
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                // Manejar errores de la base de datos
            }
        });


        mDatabase.child("last_data").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                if (dataSnapshot.exists()) {

                    int l = Integer.parseInt(dataSnapshot.child("light").getValue().toString());

                    // Convertir int a String antes de establecerlo en el TextView
                    luz_txt.setText(String.valueOf(l));

                    ProgressBar progressBar = findViewById(R.id.pb_luz);

                    // Calcula el progreso relativo dentro de los umbrales
                    int progress;
                    if (l == 0) {
                        progress = 10;

                        sendNotification("Planta en peligro", "No se esta recibiendo suficiente luz. ¡La planta está en peligro!");
                    } else {
                        progress = 100;
                    }

                    // Crea un Drawable con el color especificado
                    int color;
                    if (l == 0) {
                        color = Color.parseColor("#FF0000"); // Rojo para condiciones de luz baja
                    } else {
                        color = Color.parseColor("#00FF00"); // Verde para condiciones de luz alta
                    }

                    Drawable progressDrawable = new ClipDrawable(new ColorDrawable(color), Gravity.START, ClipDrawable.HORIZONTAL);

                    // Establece el Drawable personalizado en la ProgressBar
                    progressBar.setProgressDrawable(progressDrawable);

                    // Establece el progreso en la ProgressBar
                    progressBar.setProgress(progress);

                } else {
                    // Manejar el caso en el que los datos no existen
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                // Manejar errores de la base de datos
            }
        });







    }

    private void sendNotification(String title, String message) {
        NotificationManager notificationManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);

        // Verifica si se necesita crear un canal de notificación para versiones de Android 8.0 y superiores
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel("default_channel_id", "Default Channel", NotificationManager.IMPORTANCE_DEFAULT);
            notificationManager.createNotificationChannel(channel);
        }

        // Crea una notificación
        NotificationCompat.Builder builder = new NotificationCompat.Builder(this, "default_channel_id")
                .setSmallIcon(R.drawable.img)
                .setContentTitle(title)
                .setContentText(message)
                .setPriority(NotificationCompat.PRIORITY_DEFAULT);

        // Muestra la notificación
        notificationManager.notify(1, builder.build());
    }

}




