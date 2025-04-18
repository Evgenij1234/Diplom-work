<?php

namespace App\Controller;

use App\Entity\User;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

class TestDbOrmController extends AbstractController
{
    #[Route('/api/test-orm', name: 'api_test_orm', methods: ['GET'])]
    public function testOrm(EntityManagerInterface $em): JsonResponse
    {
        $users = $em->getRepository(User::class)->findAll();

        $result = [];

        foreach ($users as $user) {
            $result[] = [
                'id' => $user->getId(),
                'name' => $user->getName(),
                'email' => $user->getEmail(),
            ];
        }

        return $this->json([
            'message' => 'Doctrine подключена и работает!',
            'users' => $result,
        ]);
    }
}
