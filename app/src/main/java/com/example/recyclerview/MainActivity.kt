package com.example.recyclerview

import android.graphics.Color
import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView


data class ColorData(val colorName: String, val colorHex: Int)

class Adapter(private val context: Context, private val list: ArrayList<ColorData>) :
    RecyclerView.Adapter<Adapter.ViewHolder>() {

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val colorView: View = itemView.findViewById(R.id.colorView)
        val colorName: TextView = itemView.findViewById(R.id.colorName)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(context).inflate(R.layout.rview_item, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val colorData = list[position]
        holder.colorView.setBackgroundColor(colorData.colorHex)
        holder.colorName.text = colorData.colorName
    }

    override fun getItemCount(): Int {
        return list.size
    }
}


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val recyclerView: RecyclerView = findViewById(R.id.rView)

        val colorList = arrayListOf(
            ColorData("WHITE", Color.WHITE),
            ColorData("BLACK", Color.BLACK),
            ColorData("BLUE", Color.BLUE),
            ColorData("RED", Color.RED),
            ColorData("MAGENTA", Color.MAGENTA)
        )

        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = Adapter(this, colorList)
    }
}
