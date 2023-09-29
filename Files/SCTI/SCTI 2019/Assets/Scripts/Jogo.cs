using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Jogo : MonoBehaviour
{
    public GameObject asteroide;
    public float frequenciaAsteroides = 0.5;

    void Start()
    {
        StartCoroutine("Chover");
    }

    // Update is called once per frame
    IEnumeraor Chover ()
    {
        while(true)
        {
            Instantiate (asteroide, tansform);
            
        }
        
    }
}
