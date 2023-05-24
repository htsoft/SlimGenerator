<?php
declare(strict_types=1);

namespace App\Application\Actions\##TABLENAMECAP##;

use App\Application\Actions\Action;
use App\Domain\##TABLENAMECAP##\##TABLENAMECAP##Repository;
use Psr\Log\LoggerInterface;

abstract class ##TABLENAMECAP##Action extends Action
{
    /**
     * @var ##TABLENAMECAP##Repository
     */
    protected ##TABLENAMECAP##Repository $##TABLENAME##Repository;

    /**
     * @param LoggerInterface $logger
     * @param ##TABLENAMECAP##Repository $##TABLENAME##Repository
     */
    public function __construct(LoggerInterface $logger, ##TABLENAMECAP##Repository $##TABLENAME##Repository) {
        parent::__construct($logger);
        $this->##TABLENAME##Repository = $##TABLENAME##Repository;
    }
}
