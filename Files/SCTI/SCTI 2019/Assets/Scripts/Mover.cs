using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Mover : MonoBehaviour
{
public int velocidade =20;
private Rigidbody componenteRb;

    void Start()
    {
        componenteRb = GetComponent <Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        componenteRb.velocity= Vector3.up* velocidade;
    }
}
