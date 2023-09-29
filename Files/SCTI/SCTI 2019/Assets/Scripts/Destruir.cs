using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Destruir : MonoBehaviour
{
    public GameObject explosao;
    
    private void OnTriggerEnter (Collider other)
    
    {
        Instantiate(explosao, transform.position, transform.rotation);
        Destroy(GameObject);
        Destroy(other.GameObject);
    }

    }
