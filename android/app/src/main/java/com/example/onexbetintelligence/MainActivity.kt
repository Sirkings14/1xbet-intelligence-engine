package com.example.onexbetintelligence

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.media.projection.MediaProjectionManager
import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

/** Explicit, user-initiated permission scaffold. No hidden capture or account interaction. */
class MainActivity : AppCompatActivity() {
    private lateinit var status: TextView
    private val requestCode = 4107

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        status = TextView(this).apply {
            text = "Ready. Capture is off until you explicitly grant Android permission."
            textSize = 16f
            setPadding(32, 32, 32, 32)
        }
        val button = Button(this).apply {
            text = "Request one-time screen-capture permission"
            setOnClickListener { requestPermission() }
        }
        setContentView(LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(24, 48, 24, 24)
            addView(status)
            addView(button)
        })
    }

    private fun requestPermission() {
        val manager = getSystemService(Context.MEDIA_PROJECTION_SERVICE) as MediaProjectionManager
        startActivityForResult(manager.createScreenCaptureIntent(), requestCode)
    }

    @Deprecated("Minimal scaffold; migrate to Activity Result API in the capture implementation phase.")
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == this.requestCode) {
            status.text = if (resultCode == Activity.RESULT_OK && data != null)
                "Permission granted for this session. Next: capture one user-selected frame and run local OCR."
            else "Permission declined. No screen data was captured."
        }
    }
}
