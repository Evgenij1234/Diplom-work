<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

class ApiExampleController extends AbstractController
{
    #[Route('/api/example', name: 'api_example', methods: ['GET'])]
    public function index(): JsonResponse
{
    $data = [
        'message' => 'Привет, это JSON API!',
        'timestamp' => time(),
        'random_number' => rand(1, 100)
    ];

    $response = $this->json($data);
    
    // Добавляем CORS-заголовки
    $response->headers->set('Access-Control-Allow-Origin', '*');
    $response->headers->set('Access-Control-Allow-Methods', 'GET');
    
    return $response;
}
}