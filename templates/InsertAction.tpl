<?php

declare(strict_types=1);

namespace App\Application\Actions\##TABLENAMECAP##;

use App\Domain\##TABLENAMECAP##\##TABLENAMECAP##;
use Psr\Http\Message\ResponseInterface as Response;

class ##TABLENAMECAP##InsertAction extends ##TABLENAMECAP##Action
{
    /**
     * {@inheritdoc}
     */
    protected function action(): Response
    {
        // Ottiene il resto delle informazioni necessarie
        $data = $this->getFormData();
        $this->logger->info("Insert for entity ##TABLENAMECAP## ");
        $obj = new ##TABLENAMECAP##(##FIELDS##);
        $dato = $this->##TABLENAME##Repository->insert($obj);
        return $this->respondWithData($dato);
    }
}